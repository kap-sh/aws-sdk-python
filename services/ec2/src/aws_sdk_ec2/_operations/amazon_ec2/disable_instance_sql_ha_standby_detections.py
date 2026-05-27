"""Generated from Smithy shape ``com.amazonaws.ec2#DisableInstanceSqlHaStandbyDetections``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.disable_instance_sql_ha_standby_detections_request
    import aws_sdk_ec2.types.disable_instance_sql_ha_standby_detections_result


def disable_instance_sql_ha_standby_detections(
    options: OperationOptions,
    input: aws_sdk_ec2.types.disable_instance_sql_ha_standby_detections_request.DisableInstanceSqlHaStandbyDetectionsRequest,
) -> tuple[
    aws_sdk_ec2.types.disable_instance_sql_ha_standby_detections_result.DisableInstanceSqlHaStandbyDetectionsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_disable_instance_sql_ha_standby_detections(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.disable_instance_sql_ha_standby_detections_request.DisableInstanceSqlHaStandbyDetectionsRequest,
) -> tuple[
    aws_sdk_ec2.types.disable_instance_sql_ha_standby_detections_result.DisableInstanceSqlHaStandbyDetectionsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
