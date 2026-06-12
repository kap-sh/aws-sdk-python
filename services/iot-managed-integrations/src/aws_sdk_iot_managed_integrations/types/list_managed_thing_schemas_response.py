"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#ListManagedThingSchemasResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.managed_thing_schema_list_definition
    import aws_sdk_iot_managed_integrations.types.next_token


class ListManagedThingSchemasResponse(TypedDict):
    items: NotRequired[
        "aws_sdk_iot_managed_integrations.types.managed_thing_schema_list_definition.ManagedThingSchemaListDefinition"
    ]
    """<p>The list of managed thing schemas.</p>"""
    next_token: NotRequired[
        "aws_sdk_iot_managed_integrations.types.next_token.NextToken"
    ]
    """<p>A token that can be used to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListManagedThingSchemasResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import aws_sdk_iot_managed_integrations.types.managed_thing_schema_list_definition

        out["Items"] = (
            aws_sdk_iot_managed_integrations.types.managed_thing_schema_list_definition.serialize_json(
                value["items"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListManagedThingSchemasResponse:
    out: ListManagedThingSchemasResponse = {}  # type: ignore[typeddict-item]
    if "Items" in data:
        import aws_sdk_iot_managed_integrations.types.managed_thing_schema_list_definition

        out["items"] = (
            aws_sdk_iot_managed_integrations.types.managed_thing_schema_list_definition.deserialize_json(
                data["Items"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
