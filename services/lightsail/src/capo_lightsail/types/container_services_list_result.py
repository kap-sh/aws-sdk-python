"""Generated from Smithy shape ``com.amazonaws.lightsail#ContainerServicesListResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.container_service_list


class ContainerServicesListResult(TypedDict, closed=True):
    container_services: NotRequired[
        "capo_lightsail.types.container_service_list.ContainerServiceList"
    ]
    """<p>An array of objects that describe one or more container services.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerServicesListResult) -> dict:
    out: dict = {}
    if "container_services" in value:
        import capo_lightsail.types.container_service_list

        out["containerServices"] = (
            capo_lightsail.types.container_service_list.serialize_aws_json_1_1(
                value["container_services"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ContainerServicesListResult:
    out: ContainerServicesListResult = {}  # type: ignore[typeddict-item]
    if "containerServices" in data:
        import capo_lightsail.types.container_service_list

        out["container_services"] = (
            capo_lightsail.types.container_service_list.deserialize_aws_json_1_1(
                data["containerServices"]
            )
        )
    return out
