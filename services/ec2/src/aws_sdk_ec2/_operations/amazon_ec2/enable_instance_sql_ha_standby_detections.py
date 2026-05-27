"""Generated from Smithy shape ``com.amazonaws.ec2#EnableInstanceSqlHaStandbyDetections``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.enable_instance_sql_ha_standby_detections_request
    import aws_sdk_ec2.types.enable_instance_sql_ha_standby_detections_result


def enable_instance_sql_ha_standby_detections(
    options: OperationOptions,
    input: aws_sdk_ec2.types.enable_instance_sql_ha_standby_detections_request.EnableInstanceSqlHaStandbyDetectionsRequest,
) -> tuple[
    aws_sdk_ec2.types.enable_instance_sql_ha_standby_detections_result.EnableInstanceSqlHaStandbyDetectionsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_enable_instance_sql_ha_standby_detections(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.enable_instance_sql_ha_standby_detections_request.EnableInstanceSqlHaStandbyDetectionsRequest,
) -> tuple[
    aws_sdk_ec2.types.enable_instance_sql_ha_standby_detections_result.EnableInstanceSqlHaStandbyDetectionsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
