"""Generated from Smithy shape ``com.amazonaws.ec2#ReplaceIamInstanceProfileAssociation``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.replace_iam_instance_profile_association_request
    import aws_sdk_ec2.types.replace_iam_instance_profile_association_result


def replace_iam_instance_profile_association(
    options: OperationOptions,
    input: aws_sdk_ec2.types.replace_iam_instance_profile_association_request.ReplaceIamInstanceProfileAssociationRequest,
) -> tuple[
    aws_sdk_ec2.types.replace_iam_instance_profile_association_result.ReplaceIamInstanceProfileAssociationResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_replace_iam_instance_profile_association(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.replace_iam_instance_profile_association_request.ReplaceIamInstanceProfileAssociationRequest,
) -> tuple[
    aws_sdk_ec2.types.replace_iam_instance_profile_association_result.ReplaceIamInstanceProfileAssociationResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
