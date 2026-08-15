"""Generated from Smithy shape ``com.amazonaws.ec2#HealthCheckPathRequestObject``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.health_check_path_destination_request_set
    import capo_ec2.types.health_check_path_source_request_object


class HealthCheckPathRequestObject(TypedDict, closed=True):
    source: NotRequired[
        "capo_ec2.types.health_check_path_source_request_object.HealthCheckPathSourceRequestObject"
    ]
    """<p>The source for the health check path.</p>"""
    destinations: NotRequired[
        "capo_ec2.types.health_check_path_destination_request_set.HealthCheckPathDestinationRequestSet"
    ]
    """<p>The destinations for the health check path.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: HealthCheckPathRequestObject, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "source" in value:
        import capo_ec2.types.health_check_path_source_request_object

        capo_ec2.types.health_check_path_source_request_object.serialize_ec2_query(
            value["source"], pairs, f"{key_prefix}Source"
        )
    if "destinations" in value:
        import capo_ec2.types.health_check_path_destination_request_set

        capo_ec2.types.health_check_path_destination_request_set.serialize_ec2_query(
            value["destinations"], pairs, f"{key_prefix}Destination"
        )


def deserialize_ec2_query(el: Element) -> HealthCheckPathRequestObject:
    out: HealthCheckPathRequestObject = {}  # type: ignore[typeddict-item]
    child_source = el.find("Source")
    if child_source is not None:
        import capo_ec2.types.health_check_path_source_request_object

        out["source"] = (
            capo_ec2.types.health_check_path_source_request_object.deserialize_ec2_query(
                child_source
            )
        )
    child_destinations = el.find("Destination")
    if child_destinations is not None:
        import capo_ec2.types.health_check_path_destination_request_set

        out["destinations"] = (
            capo_ec2.types.health_check_path_destination_request_set.deserialize_ec2_query(
                child_destinations
            )
        )
    return out
