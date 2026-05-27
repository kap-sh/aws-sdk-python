"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeInstanceSqlHaHistoryStates``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_instance_sql_ha_history_states_request
    import aws_sdk_ec2.types.describe_instance_sql_ha_history_states_result


def describe_instance_sql_ha_history_states(
    options: OperationOptions,
    input: aws_sdk_ec2.types.describe_instance_sql_ha_history_states_request.DescribeInstanceSqlHaHistoryStatesRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_instance_sql_ha_history_states_result.DescribeInstanceSqlHaHistoryStatesResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_instance_sql_ha_history_states(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.describe_instance_sql_ha_history_states_request.DescribeInstanceSqlHaHistoryStatesRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_instance_sql_ha_history_states_result.DescribeInstanceSqlHaHistoryStatesResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
