"""Generated from Smithy shape ``com.amazonaws.ec2#HealthCheckPathResponseObject``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.health_check_path_destination_response_list
    import capo_ec2.types.health_check_path_source_response_object


class HealthCheckPathResponseObject(TypedDict, closed=True):
    source: NotRequired[
        "capo_ec2.types.health_check_path_source_response_object.HealthCheckPathSourceResponseObject"
    ]
    """<p>The source for the health check path.</p>"""
    destinations: NotRequired[
        "capo_ec2.types.health_check_path_destination_response_list.HealthCheckPathDestinationResponseList"
    ]
    """<p>The destinations for the health check path.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: HealthCheckPathResponseObject, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "source" in value:
        import capo_ec2.types.health_check_path_source_response_object

        capo_ec2.types.health_check_path_source_response_object.serialize_ec2_query(
            value["source"], pairs, f"{key_prefix}Source"
        )
    if "destinations" in value:
        import capo_ec2.types.health_check_path_destination_response_list

        capo_ec2.types.health_check_path_destination_response_list.serialize_ec2_query(
            value["destinations"], pairs, f"{key_prefix}DestinationSet"
        )


def deserialize_ec2_query(el: Element) -> HealthCheckPathResponseObject:
    out: HealthCheckPathResponseObject = {}  # type: ignore[typeddict-item]
    child_source = el.find("source")
    if child_source is not None:
        import capo_ec2.types.health_check_path_source_response_object

        out["source"] = (
            capo_ec2.types.health_check_path_source_response_object.deserialize_ec2_query(
                child_source
            )
        )
    child_destinations = el.find("destinationSet")
    if child_destinations is not None:
        import capo_ec2.types.health_check_path_destination_response_list

        out["destinations"] = (
            capo_ec2.types.health_check_path_destination_response_list.deserialize_ec2_query(
                child_destinations
            )
        )
    return out
