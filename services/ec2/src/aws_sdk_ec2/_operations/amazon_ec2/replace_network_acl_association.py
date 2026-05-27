"""Generated from Smithy shape ``com.amazonaws.ec2#ReplaceNetworkAclAssociation``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.replace_network_acl_association_request
    import aws_sdk_ec2.types.replace_network_acl_association_result


def replace_network_acl_association(
    options: OperationOptions,
    input: aws_sdk_ec2.types.replace_network_acl_association_request.ReplaceNetworkAclAssociationRequest,
) -> tuple[
    aws_sdk_ec2.types.replace_network_acl_association_result.ReplaceNetworkAclAssociationResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_replace_network_acl_association(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.replace_network_acl_association_request.ReplaceNetworkAclAssociationRequest,
) -> tuple[
    aws_sdk_ec2.types.replace_network_acl_association_result.ReplaceNetworkAclAssociationResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
