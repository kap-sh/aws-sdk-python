"""Generated from Smithy shape ``com.amazonaws.oam#UpdateLinkInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_oam.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_oam.types.include_tags
    import aws_sdk_oam.types.link_configuration
    import aws_sdk_oam.types.resource_identifier
    import aws_sdk_oam.types.resource_types_input


class UpdateLinkInput(TypedDict):
    identifier: "aws_sdk_oam.types.resource_identifier.ResourceIdentifier"
    """<p>The ARN of the link that you want to update.</p>"""
    resource_types: "aws_sdk_oam.types.resource_types_input.ResourceTypesInput"
    """<p>An array of strings that define which types of data that the source account will send to the monitoring account.</p> <p>Your input here replaces the current set of data types that are shared.</p>"""
    link_configuration: NotRequired[
        "aws_sdk_oam.types.link_configuration.LinkConfiguration"
    ]
    """<p>Use this structure to filter which metric namespaces and which log groups are to be shared from the source account to the monitoring account.</p>"""
    include_tags: NotRequired["aws_sdk_oam.types.include_tags.IncludeTags"]
    """<p>Specifies whether to include the tags associated with the link in the response after the update operation. When <code>IncludeTags</code> is set to <code>true</code> and the caller has the required permission, <code>oam:ListTagsForResource</code>, the API will return the tags for the specified resource. If the caller doesn't have the required permission, <code>oam:ListTagsForResource</code>, the API will raise an exception. </p> <p>The default value is <code>false</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateLinkInput) -> dict:
    out: dict = {}
    out["Identifier"] = value["identifier"]
    import aws_sdk_oam.types.resource_types_input

    out["ResourceTypes"] = aws_sdk_oam.types.resource_types_input.serialize_json(
        value["resource_types"]
    )
    if "link_configuration" in value:
        import aws_sdk_oam.types.link_configuration

        out["LinkConfiguration"] = aws_sdk_oam.types.link_configuration.serialize_json(
            value["link_configuration"]
        )
    if "include_tags" in value:
        out["IncludeTags"] = value["include_tags"]
    return out


def deserialize_json(data: dict) -> UpdateLinkInput:
    out: UpdateLinkInput = {}  # type: ignore[typeddict-item]
    if "Identifier" in data:
        out["identifier"] = data["Identifier"]
    else:
        raise DeserializationError("UpdateLinkInput.identifier required")
    if "ResourceTypes" in data:
        import aws_sdk_oam.types.resource_types_input

        out["resource_types"] = aws_sdk_oam.types.resource_types_input.deserialize_json(
            data["ResourceTypes"]
        )
    else:
        raise DeserializationError("UpdateLinkInput.resource_types required")
    if "LinkConfiguration" in data:
        import aws_sdk_oam.types.link_configuration

        out["link_configuration"] = (
            aws_sdk_oam.types.link_configuration.deserialize_json(
                data["LinkConfiguration"]
            )
        )
    if "IncludeTags" in data:
        out["include_tags"] = data["IncludeTags"]
    return out
