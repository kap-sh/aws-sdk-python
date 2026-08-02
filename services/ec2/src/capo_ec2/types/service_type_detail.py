"""Generated from Smithy shape ``com.amazonaws.ec2#ServiceTypeDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.service_type


class ServiceTypeDetail(TypedDict, closed=True):
    service_type: NotRequired["capo_ec2.types.service_type.ServiceType"]
    """<p>The type of service.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ServiceTypeDetail, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "service_type" in value:
        import capo_ec2.types.service_type

        capo_ec2.types.service_type.serialize_ec2_query(
            value["service_type"], pairs, f"{key_prefix}ServiceType"
        )


def deserialize_ec2_query(el: Element) -> ServiceTypeDetail:
    out: ServiceTypeDetail = {}  # type: ignore[typeddict-item]
    child_service_type = el.find("ServiceType")
    if child_service_type is not None:
        import capo_ec2.types.service_type

        out["service_type"] = capo_ec2.types.service_type.deserialize_ec2_query(
            child_service_type
        )
    return out
