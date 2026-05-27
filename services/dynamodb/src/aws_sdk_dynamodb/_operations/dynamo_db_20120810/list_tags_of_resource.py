"""Generated from Smithy shape ``com.amazonaws.dynamodb#ListTagsOfResource``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_dynamodb._auth._signers
from aws_sdk_dynamodb._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.list_tags_of_resource_input
    import aws_sdk_dynamodb.types.list_tags_of_resource_output


def list_tags_of_resource(
    options: OperationOptions,
    input: aws_sdk_dynamodb.types.list_tags_of_resource_input.ListTagsOfResourceInput,
) -> tuple[
    aws_sdk_dynamodb.types.list_tags_of_resource_output.ListTagsOfResourceOutput,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_list_tags_of_resource(
    options: AsyncOperationOptions,
    input: aws_sdk_dynamodb.types.list_tags_of_resource_input.ListTagsOfResourceInput,
) -> tuple[
    aws_sdk_dynamodb.types.list_tags_of_resource_output.ListTagsOfResourceOutput,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
