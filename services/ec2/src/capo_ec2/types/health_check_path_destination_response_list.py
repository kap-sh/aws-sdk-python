"""Generated from Smithy shape ``com.amazonaws.ec2#HealthCheckPathDestinationResponseList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.health_check_path_destination_response_object

HealthCheckPathDestinationResponseList: TypeAlias = list[
    "capo_ec2.types.health_check_path_destination_response_object.HealthCheckPathDestinationResponseObject"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: HealthCheckPathDestinationResponseList,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.health_check_path_destination_response_object

        capo_ec2.types.health_check_path_destination_response_object.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> HealthCheckPathDestinationResponseList:
    import capo_ec2.types.health_check_path_destination_response_object

    out: HealthCheckPathDestinationResponseList = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.health_check_path_destination_response_object.deserialize_ec2_query(
                child
            )
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> HealthCheckPathDestinationResponseList:
    import capo_ec2.types.health_check_path_destination_response_object

    out: HealthCheckPathDestinationResponseList = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.health_check_path_destination_response_object.deserialize_ec2_query(
                child
            )
        )
    return out
