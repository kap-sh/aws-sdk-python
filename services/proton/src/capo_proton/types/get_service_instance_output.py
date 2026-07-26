"""Generated from Smithy shape ``com.amazonaws.proton#GetServiceInstanceOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_proton.errors import DeserializationError

if TYPE_CHECKING:
    import capo_proton.types.service_instance


class GetServiceInstanceOutput(TypedDict, closed=True):
    service_instance: "capo_proton.types.service_instance.ServiceInstance"
    """<p>The detailed data of the requested service instance.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetServiceInstanceOutput) -> dict:
    out: dict = {}
    import capo_proton.types.service_instance

    out["serviceInstance"] = capo_proton.types.service_instance.serialize_aws_json_1_0(
        value["service_instance"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetServiceInstanceOutput:
    out: GetServiceInstanceOutput = {}  # type: ignore[typeddict-item]
    if "serviceInstance" in data:
        import capo_proton.types.service_instance

        out["service_instance"] = (
            capo_proton.types.service_instance.deserialize_aws_json_1_0(
                data["serviceInstance"]
            )
        )
    else:
        raise DeserializationError("GetServiceInstanceOutput.service_instance required")
    return out
