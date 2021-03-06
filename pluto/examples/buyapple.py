#!/usr/bin/env python
#
# Copyright 2014 Quantopian, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from pluto import api


def initialize(context):
    context.asset = api.symbol('AAPL')

    # Explicitly set the commission/slippage to the "old" value until we can
    # rebuild example data.
    # github.com/quantopian/zipline/blob/master/tests/resources/
    # rebuild_example_data#L105
    # context.set_commission(commission.PerShare(cost=.0075, min_trade_cost=1.0))
    # context.set_slippage(slippage.VolumeShareSlippage())


def handle_data(context, data):
    api.order(context.asset, 10)
    api.record(AAPL=data.current(context.asset, 'price'))


def _test_args():
    """Extra arguments to use when zipline's automated tests run this example.
    """
    import pandas as pd

    return {
        'start': pd.Timestamp('2014-01-01', tz='utc'),
        'end': pd.Timestamp('2014-11-01', tz='utc'),
        'capital_base': 1e7,
        'max_leverage': 1.0,
        'look_back': None,
        'data_frequency': 'daily'
    }
