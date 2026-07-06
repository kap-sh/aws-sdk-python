"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#ListChannelHandshakesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_partnercentral_channel.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_channel.types.associated_resource_identifier_list
    import aws_sdk_partnercentral_channel.types.catalog
    import aws_sdk_partnercentral_channel.types.handshake_status_list
    import aws_sdk_partnercentral_channel.types.handshake_type
    import aws_sdk_partnercentral_channel.types.list_channel_handshakes_type_filters
    import aws_sdk_partnercentral_channel.types.list_channel_handshakes_type_sort
    import aws_sdk_partnercentral_channel.types.next_token
    import aws_sdk_partnercentral_channel.types.participant_type


class ListChannelHandshakesRequest(TypedDict, closed=True):
    handshake_type: "aws_sdk_partnercentral_channel.types.handshake_type.HandshakeType"
    """<p>Filter results by handshake type.</p>"""
    catalog: "aws_sdk_partnercentral_channel.types.catalog.Catalog"
    """<p>The catalog identifier to filter handshakes.</p>"""
    participant_type: (
        "aws_sdk_partnercentral_channel.types.participant_type.ParticipantType"
    )
    """<p>Filter by participant type (sender or receiver).</p>"""
    max_results: "int"
    """<p>The maximum number of results to return in a single call.</p>"""
    statuses: NotRequired[
        "aws_sdk_partnercentral_channel.types.handshake_status_list.HandshakeStatusList"
    ]
    """<p>Filter results by handshake status.</p>"""
    associated_resource_identifiers: NotRequired[
        "aws_sdk_partnercentral_channel.types.associated_resource_identifier_list.AssociatedResourceIdentifierList"
    ]
    """<p>Filter by associated resource identifiers.</p>"""
    handshake_type_filters: NotRequired[
        "aws_sdk_partnercentral_channel.types.list_channel_handshakes_type_filters.ListChannelHandshakesTypeFilters"
    ]
    """<p>Type-specific filters for handshakes.</p>"""
    handshake_type_sort: NotRequired[
        "aws_sdk_partnercentral_channel.types.list_channel_handshakes_type_sort.ListChannelHandshakesTypeSort"
    ]
    """<p>Type-specific sorting options for handshakes.</p>"""
    next_token: NotRequired["aws_sdk_partnercentral_channel.types.next_token.NextToken"]
    """<p>Token for retrieving the next page of results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListChannelHandshakesRequest) -> dict:
    out: dict = {}
    import aws_sdk_partnercentral_channel.types.handshake_type

    out["handshakeType"] = (
        aws_sdk_partnercentral_channel.types.handshake_type.serialize_aws_json_1_0(
            value["handshake_type"]
        )
    )
    out["catalog"] = value["catalog"]
    import aws_sdk_partnercentral_channel.types.participant_type

    out["participantType"] = (
        aws_sdk_partnercentral_channel.types.participant_type.serialize_aws_json_1_0(
            value["participant_type"]
        )
    )
    out["maxResults"] = value.get("max_results", 20)
    if "statuses" in value:
        import aws_sdk_partnercentral_channel.types.handshake_status_list

        out["statuses"] = (
            aws_sdk_partnercentral_channel.types.handshake_status_list.serialize_aws_json_1_0(
                value["statuses"]
            )
        )
    if "associated_resource_identifiers" in value:
        import aws_sdk_partnercentral_channel.types.associated_resource_identifier_list

        out["associatedResourceIdentifiers"] = (
            aws_sdk_partnercentral_channel.types.associated_resource_identifier_list.serialize_aws_json_1_0(
                value["associated_resource_identifiers"]
            )
        )
    if "handshake_type_filters" in value:
        import aws_sdk_partnercentral_channel.types.list_channel_handshakes_type_filters

        out["handshakeTypeFilters"] = (
            aws_sdk_partnercentral_channel.types.list_channel_handshakes_type_filters.serialize_aws_json_1_0(
                value["handshake_type_filters"]
            )
        )
    if "handshake_type_sort" in value:
        import aws_sdk_partnercentral_channel.types.list_channel_handshakes_type_sort

        out["handshakeTypeSort"] = (
            aws_sdk_partnercentral_channel.types.list_channel_handshakes_type_sort.serialize_aws_json_1_0(
                value["handshake_type_sort"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListChannelHandshakesRequest:
    out: ListChannelHandshakesRequest = {}  # type: ignore[typeddict-item]
    if "handshakeType" in data:
        import aws_sdk_partnercentral_channel.types.handshake_type

        out["handshake_type"] = (
            aws_sdk_partnercentral_channel.types.handshake_type.deserialize_aws_json_1_0(
                data["handshakeType"]
            )
        )
    else:
        raise DeserializationError(
            "ListChannelHandshakesRequest.handshake_type required"
        )
    if "catalog" in data:
        out["catalog"] = data["catalog"]
    else:
        raise DeserializationError("ListChannelHandshakesRequest.catalog required")
    if "participantType" in data:
        import aws_sdk_partnercentral_channel.types.participant_type

        out["participant_type"] = (
            aws_sdk_partnercentral_channel.types.participant_type.deserialize_aws_json_1_0(
                data["participantType"]
            )
        )
    else:
        raise DeserializationError(
            "ListChannelHandshakesRequest.participant_type required"
        )
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    else:
        out["max_results"] = 20
    if "statuses" in data:
        import aws_sdk_partnercentral_channel.types.handshake_status_list

        out["statuses"] = (
            aws_sdk_partnercentral_channel.types.handshake_status_list.deserialize_aws_json_1_0(
                data["statuses"]
            )
        )
    if "associatedResourceIdentifiers" in data:
        import aws_sdk_partnercentral_channel.types.associated_resource_identifier_list

        out["associated_resource_identifiers"] = (
            aws_sdk_partnercentral_channel.types.associated_resource_identifier_list.deserialize_aws_json_1_0(
                data["associatedResourceIdentifiers"]
            )
        )
    if "handshakeTypeFilters" in data:
        import aws_sdk_partnercentral_channel.types.list_channel_handshakes_type_filters

        out["handshake_type_filters"] = (
            aws_sdk_partnercentral_channel.types.list_channel_handshakes_type_filters.deserialize_aws_json_1_0(
                data["handshakeTypeFilters"]
            )
        )
    if "handshakeTypeSort" in data:
        import aws_sdk_partnercentral_channel.types.list_channel_handshakes_type_sort

        out["handshake_type_sort"] = (
            aws_sdk_partnercentral_channel.types.list_channel_handshakes_type_sort.deserialize_aws_json_1_0(
                data["handshakeTypeSort"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
