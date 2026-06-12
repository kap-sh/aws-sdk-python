"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#ListSchemaVersionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.next_token
    import aws_sdk_iot_managed_integrations.types.schema_version_list


class ListSchemaVersionsResponse(TypedDict):
    items: NotRequired[
        "aws_sdk_iot_managed_integrations.types.schema_version_list.SchemaVersionList"
    ]
    """<p>The list of schema versions.</p>"""
    next_token: NotRequired[
        "aws_sdk_iot_managed_integrations.types.next_token.NextToken"
    ]
    """<p>A token that can be used to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSchemaVersionsResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import aws_sdk_iot_managed_integrations.types.schema_version_list

        out["Items"] = (
            aws_sdk_iot_managed_integrations.types.schema_version_list.serialize_json(
                value["items"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSchemaVersionsResponse:
    out: ListSchemaVersionsResponse = {}  # type: ignore[typeddict-item]
    if "Items" in data:
        import aws_sdk_iot_managed_integrations.types.schema_version_list

        out["items"] = (
            aws_sdk_iot_managed_integrations.types.schema_version_list.deserialize_json(
                data["Items"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
