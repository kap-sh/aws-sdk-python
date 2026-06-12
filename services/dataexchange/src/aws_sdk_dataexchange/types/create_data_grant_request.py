"""Generated from Smithy shape ``com.amazonaws.dataexchange#CreateDataGrantRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_dataexchange.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dataexchange.types.data_grant_name
    import aws_sdk_dataexchange.types.description
    import aws_sdk_dataexchange.types.grant_distribution_scope
    import aws_sdk_dataexchange.types.id
    import aws_sdk_dataexchange.types.map_of__string
    import aws_sdk_dataexchange.types.receiver_principal
    import aws_sdk_dataexchange.types.timestamp


class CreateDataGrantRequest(TypedDict):
    name: "aws_sdk_dataexchange.types.data_grant_name.DataGrantName"
    """<p>The name of the data grant.</p>"""
    grant_distribution_scope: (
        "aws_sdk_dataexchange.types.grant_distribution_scope.GrantDistributionScope"
    )
    """<p>The distribution scope of the data grant.</p>"""
    receiver_principal: (
        "aws_sdk_dataexchange.types.receiver_principal.ReceiverPrincipal"
    )
    """<p>The Amazon Web Services account ID of the data grant receiver.</p>"""
    source_data_set_id: "aws_sdk_dataexchange.types.id.Id"
    """<p>The ID of the data set used to create the data grant.</p>"""
    ends_at: NotRequired["aws_sdk_dataexchange.types.timestamp.Timestamp"]
    """<p>The timestamp of when access to the associated data set ends.</p>"""
    description: NotRequired["aws_sdk_dataexchange.types.description.Description"]
    """<p>The description of the data grant.</p>"""
    tags: NotRequired["aws_sdk_dataexchange.types.map_of__string.MapOf__string"]
    """<p>The tags to add to the data grant. A tag is a key-value pair.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDataGrantRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["GrantDistributionScope"] = value["grant_distribution_scope"]
    out["ReceiverPrincipal"] = value["receiver_principal"]
    out["SourceDataSetId"] = value["source_data_set_id"]
    if "ends_at" in value:
        import aws_sdk_dataexchange.types.timestamp

        out["EndsAt"] = aws_sdk_dataexchange.types.timestamp.serialize_json(
            value["ends_at"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "tags" in value:
        import aws_sdk_dataexchange.types.map_of__string

        out["Tags"] = aws_sdk_dataexchange.types.map_of__string.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateDataGrantRequest:
    out: CreateDataGrantRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateDataGrantRequest.name required")
    if "GrantDistributionScope" in data:
        out["grant_distribution_scope"] = data["GrantDistributionScope"]
    else:
        raise DeserializationError(
            "CreateDataGrantRequest.grant_distribution_scope required"
        )
    if "ReceiverPrincipal" in data:
        out["receiver_principal"] = data["ReceiverPrincipal"]
    else:
        raise DeserializationError("CreateDataGrantRequest.receiver_principal required")
    if "SourceDataSetId" in data:
        out["source_data_set_id"] = data["SourceDataSetId"]
    else:
        raise DeserializationError("CreateDataGrantRequest.source_data_set_id required")
    if "EndsAt" in data:
        import aws_sdk_dataexchange.types.timestamp

        out["ends_at"] = aws_sdk_dataexchange.types.timestamp.deserialize_json(
            data["EndsAt"]
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "Tags" in data:
        import aws_sdk_dataexchange.types.map_of__string

        out["tags"] = aws_sdk_dataexchange.types.map_of__string.deserialize_json(
            data["Tags"]
        )
    return out
