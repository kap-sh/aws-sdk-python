"""Generated from Smithy shape ``com.amazonaws.lambda#ListCapacityProvidersResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lambda.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lambda.types.capacity_providers_list
    import aws_sdk_lambda.types.string


class ListCapacityProvidersResponse(TypedDict):
    capacity_providers: (
        "aws_sdk_lambda.types.capacity_providers_list.CapacityProvidersList"
    )
    """<p>A list of capacity providers in your account.</p>"""
    next_marker: NotRequired["aws_sdk_lambda.types.string.String"]
    """<p>The pagination token that's included if more results are available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCapacityProvidersResponse) -> dict:
    out: dict = {}
    import aws_sdk_lambda.types.capacity_providers_list

    out["CapacityProviders"] = (
        aws_sdk_lambda.types.capacity_providers_list.serialize_json(
            value["capacity_providers"]
        )
    )
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    return out


def deserialize_json(data: dict) -> ListCapacityProvidersResponse:
    out: ListCapacityProvidersResponse = {}  # type: ignore[typeddict-item]
    if "CapacityProviders" in data:
        import aws_sdk_lambda.types.capacity_providers_list

        out["capacity_providers"] = (
            aws_sdk_lambda.types.capacity_providers_list.deserialize_json(
                data["CapacityProviders"]
            )
        )
    else:
        raise DeserializationError(
            "ListCapacityProvidersResponse.capacity_providers required"
        )
    if "NextMarker" in data:
        out["next_marker"] = data["NextMarker"]
    return out
