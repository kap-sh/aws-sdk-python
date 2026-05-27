"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyInstanceMetadataDefaults``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.modify_instance_metadata_defaults_request
    import aws_sdk_ec2.types.modify_instance_metadata_defaults_result


def modify_instance_metadata_defaults(
    options: OperationOptions,
    input: aws_sdk_ec2.types.modify_instance_metadata_defaults_request.ModifyInstanceMetadataDefaultsRequest,
) -> tuple[
    aws_sdk_ec2.types.modify_instance_metadata_defaults_result.ModifyInstanceMetadataDefaultsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_modify_instance_metadata_defaults(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.modify_instance_metadata_defaults_request.ModifyInstanceMetadataDefaultsRequest,
) -> tuple[
    aws_sdk_ec2.types.modify_instance_metadata_defaults_result.ModifyInstanceMetadataDefaultsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
