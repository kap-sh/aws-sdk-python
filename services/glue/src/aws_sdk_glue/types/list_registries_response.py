"""Generated from Smithy shape ``com.amazonaws.glue#ListRegistriesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.registry_list_definition
    import aws_sdk_glue.types.schema_registry_token_string


class ListRegistriesResponse(TypedDict, closed=True):
    registries: NotRequired[
        "aws_sdk_glue.types.registry_list_definition.RegistryListDefinition"
    ]
    """<p>An array of <code>RegistryDetailedListItem</code> objects containing minimal details of each registry.</p>"""
    next_token: NotRequired[
        "aws_sdk_glue.types.schema_registry_token_string.SchemaRegistryTokenString"
    ]
    """<p>A continuation token for paginating the returned list of tokens, returned if the current segment of the list is not the last.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListRegistriesResponse) -> dict:
    out: dict = {}
    if "registries" in value:
        import aws_sdk_glue.types.registry_list_definition

        out["Registries"] = (
            aws_sdk_glue.types.registry_list_definition.serialize_aws_json_1_1(
                value["registries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListRegistriesResponse:
    out: ListRegistriesResponse = {}  # type: ignore[typeddict-item]
    if "Registries" in data:
        import aws_sdk_glue.types.registry_list_definition

        out["registries"] = (
            aws_sdk_glue.types.registry_list_definition.deserialize_aws_json_1_1(
                data["Registries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
