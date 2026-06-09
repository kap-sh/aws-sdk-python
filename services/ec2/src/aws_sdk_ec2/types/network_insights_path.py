"""Generated from Smithy shape ``com.amazonaws.ec2#NetworkInsightsPath``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.ip_address
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.network_insights_path_id
    import aws_sdk_ec2.types.path_filter
    import aws_sdk_ec2.types.protocol
    import aws_sdk_ec2.types.resource_arn
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class NetworkInsightsPath(TypedDict):
    network_insights_path_id: NotRequired[
        "aws_sdk_ec2.types.network_insights_path_id.NetworkInsightsPathId"
    ]
    """<p>The ID of the path.</p>"""
    network_insights_path_arn: NotRequired["aws_sdk_ec2.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the path.</p>"""
    created_date: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The time stamp when the path was created.</p>"""
    source: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the source.</p>"""
    destination: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the destination.</p>"""
    source_arn: NotRequired["aws_sdk_ec2.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the source.</p>"""
    destination_arn: NotRequired["aws_sdk_ec2.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the destination.</p>"""
    source_ip: NotRequired["aws_sdk_ec2.types.ip_address.IpAddress"]
    """<p>The IP address of the source.</p>"""
    destination_ip: NotRequired["aws_sdk_ec2.types.ip_address.IpAddress"]
    """<p>The IP address of the destination.</p>"""
    protocol: NotRequired["aws_sdk_ec2.types.protocol.Protocol"]
    """<p>The protocol.</p>"""
    destination_port: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The destination port.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags associated with the path.</p>"""
    filter_at_source: NotRequired["aws_sdk_ec2.types.path_filter.PathFilter"]
    """<p>Scopes the analysis to network paths that match specific filters at the source.</p>"""
    filter_at_destination: NotRequired["aws_sdk_ec2.types.path_filter.PathFilter"]
    """<p>Scopes the analysis to network paths that match specific filters at the destination.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: NetworkInsightsPath, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "network_insights_path_id" in value:
        pairs.append(
            (f"{prefix}.NetworkInsightsPathId", str(value["network_insights_path_id"]))
        )
    if "network_insights_path_arn" in value:
        pairs.append(
            (
                f"{prefix}.NetworkInsightsPathArn",
                str(value["network_insights_path_arn"]),
            )
        )
    if "created_date" in value:
        import aws_sdk_ec2.types.millisecond_date_time

        aws_sdk_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["created_date"], pairs, f"{prefix}.CreatedDate"
        )
    if "source" in value:
        pairs.append((f"{prefix}.Source", str(value["source"])))
    if "destination" in value:
        pairs.append((f"{prefix}.Destination", str(value["destination"])))
    if "source_arn" in value:
        pairs.append((f"{prefix}.SourceArn", str(value["source_arn"])))
    if "destination_arn" in value:
        pairs.append((f"{prefix}.DestinationArn", str(value["destination_arn"])))
    if "source_ip" in value:
        pairs.append((f"{prefix}.SourceIp", str(value["source_ip"])))
    if "destination_ip" in value:
        pairs.append((f"{prefix}.DestinationIp", str(value["destination_ip"])))
    if "protocol" in value:
        import aws_sdk_ec2.types.protocol

        aws_sdk_ec2.types.protocol.serialize_ec2_query(
            value["protocol"], pairs, f"{prefix}.Protocol"
        )
    if "destination_port" in value:
        pairs.append((f"{prefix}.DestinationPort", str(value["destination_port"])))
    if "tags" in value:
        import aws_sdk_ec2.types.tag_list

        aws_sdk_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{prefix}.TagSet"
        )
    if "filter_at_source" in value:
        import aws_sdk_ec2.types.path_filter

        aws_sdk_ec2.types.path_filter.serialize_ec2_query(
            value["filter_at_source"], pairs, f"{prefix}.FilterAtSource"
        )
    if "filter_at_destination" in value:
        import aws_sdk_ec2.types.path_filter

        aws_sdk_ec2.types.path_filter.serialize_ec2_query(
            value["filter_at_destination"], pairs, f"{prefix}.FilterAtDestination"
        )


def deserialize_ec2_query(el: Element) -> NetworkInsightsPath:
    out: NetworkInsightsPath = {}  # type: ignore[typeddict-item]
    child_network_insights_path_id = el.find("NetworkInsightsPathId")
    if child_network_insights_path_id is not None:
        out["network_insights_path_id"] = str(child_network_insights_path_id.text or "")
    child_network_insights_path_arn = el.find("NetworkInsightsPathArn")
    if child_network_insights_path_arn is not None:
        out["network_insights_path_arn"] = str(
            child_network_insights_path_arn.text or ""
        )
    child_created_date = el.find("CreatedDate")
    if child_created_date is not None:
        import aws_sdk_ec2.types.millisecond_date_time

        out["created_date"] = (
            aws_sdk_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_created_date
            )
        )
    child_source = el.find("Source")
    if child_source is not None:
        out["source"] = str(child_source.text or "")
    child_destination = el.find("Destination")
    if child_destination is not None:
        out["destination"] = str(child_destination.text or "")
    child_source_arn = el.find("SourceArn")
    if child_source_arn is not None:
        out["source_arn"] = str(child_source_arn.text or "")
    child_destination_arn = el.find("DestinationArn")
    if child_destination_arn is not None:
        out["destination_arn"] = str(child_destination_arn.text or "")
    child_source_ip = el.find("SourceIp")
    if child_source_ip is not None:
        out["source_ip"] = str(child_source_ip.text or "")
    child_destination_ip = el.find("DestinationIp")
    if child_destination_ip is not None:
        out["destination_ip"] = str(child_destination_ip.text or "")
    child_protocol = el.find("Protocol")
    if child_protocol is not None:
        import aws_sdk_ec2.types.protocol

        out["protocol"] = aws_sdk_ec2.types.protocol.deserialize_ec2_query(
            child_protocol
        )
    child_destination_port = el.find("DestinationPort")
    if child_destination_port is not None:
        out["destination_port"] = int(child_destination_port.text or "")
    if el.find("TagSet") is not None:
        import aws_sdk_ec2.types.tag_list

        out["tags"] = aws_sdk_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    child_filter_at_source = el.find("FilterAtSource")
    if child_filter_at_source is not None:
        import aws_sdk_ec2.types.path_filter

        out["filter_at_source"] = aws_sdk_ec2.types.path_filter.deserialize_ec2_query(
            child_filter_at_source
        )
    child_filter_at_destination = el.find("FilterAtDestination")
    if child_filter_at_destination is not None:
        import aws_sdk_ec2.types.path_filter

        out["filter_at_destination"] = (
            aws_sdk_ec2.types.path_filter.deserialize_ec2_query(
                child_filter_at_destination
            )
        )
    return out
