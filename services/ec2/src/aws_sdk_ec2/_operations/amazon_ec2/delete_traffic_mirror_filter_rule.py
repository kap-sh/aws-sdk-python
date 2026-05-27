"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteTrafficMirrorFilterRule``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.delete_traffic_mirror_filter_rule_request
    import aws_sdk_ec2.types.delete_traffic_mirror_filter_rule_result


def delete_traffic_mirror_filter_rule(
    options: OperationOptions,
    input: aws_sdk_ec2.types.delete_traffic_mirror_filter_rule_request.DeleteTrafficMirrorFilterRuleRequest,
) -> tuple[
    aws_sdk_ec2.types.delete_traffic_mirror_filter_rule_result.DeleteTrafficMirrorFilterRuleResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_delete_traffic_mirror_filter_rule(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.delete_traffic_mirror_filter_rule_request.DeleteTrafficMirrorFilterRuleRequest,
) -> tuple[
    aws_sdk_ec2.types.delete_traffic_mirror_filter_rule_result.DeleteTrafficMirrorFilterRuleResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
