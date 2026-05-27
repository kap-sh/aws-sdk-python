"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyTrafficMirrorSession``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.modify_traffic_mirror_session_request
    import aws_sdk_ec2.types.modify_traffic_mirror_session_result


def modify_traffic_mirror_session(
    options: OperationOptions,
    input: aws_sdk_ec2.types.modify_traffic_mirror_session_request.ModifyTrafficMirrorSessionRequest,
) -> tuple[
    aws_sdk_ec2.types.modify_traffic_mirror_session_result.ModifyTrafficMirrorSessionResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_modify_traffic_mirror_session(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.modify_traffic_mirror_session_request.ModifyTrafficMirrorSessionRequest,
) -> tuple[
    aws_sdk_ec2.types.modify_traffic_mirror_session_result.ModifyTrafficMirrorSessionResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
