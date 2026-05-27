"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyTrafficMirrorFilterRule``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.modify_traffic_mirror_filter_rule_request
    import aws_sdk_ec2.types.modify_traffic_mirror_filter_rule_result


def modify_traffic_mirror_filter_rule(
    options: OperationOptions,
    input: aws_sdk_ec2.types.modify_traffic_mirror_filter_rule_request.ModifyTrafficMirrorFilterRuleRequest,
) -> tuple[
    aws_sdk_ec2.types.modify_traffic_mirror_filter_rule_result.ModifyTrafficMirrorFilterRuleResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_modify_traffic_mirror_filter_rule(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.modify_traffic_mirror_filter_rule_request.ModifyTrafficMirrorFilterRuleRequest,
) -> tuple[
    aws_sdk_ec2.types.modify_traffic_mirror_filter_rule_result.ModifyTrafficMirrorFilterRuleResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
