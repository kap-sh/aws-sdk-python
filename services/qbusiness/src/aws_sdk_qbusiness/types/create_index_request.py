"""Generated from Smithy shape ``com.amazonaws.qbusiness#CreateIndexRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_qbusiness.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.application_id
    import aws_sdk_qbusiness.types.client_token
    import aws_sdk_qbusiness.types.description
    import aws_sdk_qbusiness.types.index_capacity_configuration
    import aws_sdk_qbusiness.types.index_name
    import aws_sdk_qbusiness.types.index_type
    import aws_sdk_qbusiness.types.tags


class CreateIndexRequest(TypedDict):
    application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId"
    """<p>The identifier of the Amazon Q Business application using the index.</p>"""
    display_name: "aws_sdk_qbusiness.types.index_name.IndexName"
    """<p>A name for the Amazon Q Business index.</p>"""
    description: NotRequired["aws_sdk_qbusiness.types.description.Description"]
    """<p>A description for the Amazon Q Business index.</p>"""
    type: NotRequired["aws_sdk_qbusiness.types.index_type.IndexType"]
    r"""<p>The index type that's suitable for your needs. For more information on what's included in each type of index, see <a href=\"https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/tiers.html#index-tiers\">Amazon Q Business tiers</a>.</p>"""
    tags: NotRequired["aws_sdk_qbusiness.types.tags.Tags"]
    """<p>A list of key-value pairs that identify or categorize the index. You can also use tags to help control access to the index. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: _ . : / = + - @.</p>"""
    capacity_configuration: NotRequired[
        "aws_sdk_qbusiness.types.index_capacity_configuration.IndexCapacityConfiguration"
    ]
    """<p>The capacity units you want to provision for your index. You can add and remove capacity to fit your usage needs.</p>"""
    client_token: NotRequired["aws_sdk_qbusiness.types.client_token.ClientToken"]
    """<p>A token that you provide to identify the request to create an index. Multiple calls to the <code>CreateIndex</code> API with the same client token will create only one index.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateIndexRequest) -> dict:
    out: dict = {}
    out["displayName"] = value["display_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "type" in value:
        import aws_sdk_qbusiness.types.index_type

        out["type"] = aws_sdk_qbusiness.types.index_type.serialize_json(value["type"])
    if "tags" in value:
        import aws_sdk_qbusiness.types.tags

        out["tags"] = aws_sdk_qbusiness.types.tags.serialize_json(value["tags"])
    if "capacity_configuration" in value:
        import aws_sdk_qbusiness.types.index_capacity_configuration

        out["capacityConfiguration"] = (
            aws_sdk_qbusiness.types.index_capacity_configuration.serialize_json(
                value["capacity_configuration"]
            )
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateIndexRequest:
    out: CreateIndexRequest = {}  # type: ignore[typeddict-item]
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    else:
        raise DeserializationError("CreateIndexRequest.display_name required")
    if "description" in data:
        out["description"] = data["description"]
    if "type" in data:
        import aws_sdk_qbusiness.types.index_type

        out["type"] = aws_sdk_qbusiness.types.index_type.deserialize_json(data["type"])
    if "tags" in data:
        import aws_sdk_qbusiness.types.tags

        out["tags"] = aws_sdk_qbusiness.types.tags.deserialize_json(data["tags"])
    if "capacityConfiguration" in data:
        import aws_sdk_qbusiness.types.index_capacity_configuration

        out["capacity_configuration"] = (
            aws_sdk_qbusiness.types.index_capacity_configuration.deserialize_json(
                data["capacityConfiguration"]
            )
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
