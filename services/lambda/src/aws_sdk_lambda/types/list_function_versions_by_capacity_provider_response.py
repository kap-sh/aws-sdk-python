"""Generated from Smithy shape ``com.amazonaws.lambda#ListFunctionVersionsByCapacityProviderResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_lambda.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lambda.types.capacity_provider_arn
    import aws_sdk_lambda.types.function_versions_by_capacity_provider_list
    import aws_sdk_lambda.types.string


class ListFunctionVersionsByCapacityProviderResponse(TypedDict):
    capacity_provider_arn: (
        "aws_sdk_lambda.types.capacity_provider_arn.CapacityProviderArn"
    )
    """<p>The Amazon Resource Name (ARN) of the capacity provider.</p>"""
    function_versions: "aws_sdk_lambda.types.function_versions_by_capacity_provider_list.FunctionVersionsByCapacityProviderList"
    """<p>A list of function versions that use the specified capacity provider.</p>"""
    next_marker: NotRequired["aws_sdk_lambda.types.string.String"]
    """<p>The pagination token that's included if more results are available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFunctionVersionsByCapacityProviderResponse) -> dict:
    out: dict = {}
    out["CapacityProviderArn"] = value["capacity_provider_arn"]
    import aws_sdk_lambda.types.function_versions_by_capacity_provider_list

    out["FunctionVersions"] = (
        aws_sdk_lambda.types.function_versions_by_capacity_provider_list.serialize_json(
            value["function_versions"]
        )
    )
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    return out


def deserialize_json(data: dict) -> ListFunctionVersionsByCapacityProviderResponse:
    out: ListFunctionVersionsByCapacityProviderResponse = {}  # type: ignore[typeddict-item]
    if "CapacityProviderArn" in data:
        out["capacity_provider_arn"] = data["CapacityProviderArn"]
    else:
        raise DeserializationError(
            "ListFunctionVersionsByCapacityProviderResponse.capacity_provider_arn required"
        )
    if "FunctionVersions" in data:
        import aws_sdk_lambda.types.function_versions_by_capacity_provider_list

        out["function_versions"] = (
            aws_sdk_lambda.types.function_versions_by_capacity_provider_list.deserialize_json(
                data["FunctionVersions"]
            )
        )
    else:
        raise DeserializationError(
            "ListFunctionVersionsByCapacityProviderResponse.function_versions required"
        )
    if "NextMarker" in data:
        out["next_marker"] = data["NextMarker"]
    return out
