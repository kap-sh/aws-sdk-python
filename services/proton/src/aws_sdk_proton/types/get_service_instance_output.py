"""Generated from Smithy shape ``com.amazonaws.proton#GetServiceInstanceOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_proton.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_proton.types.service_instance


class GetServiceInstanceOutput(TypedDict, closed=True):
    service_instance: "aws_sdk_proton.types.service_instance.ServiceInstance"
    """<p>The detailed data of the requested service instance.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetServiceInstanceOutput) -> dict:
    out: dict = {}
    import aws_sdk_proton.types.service_instance

    out["serviceInstance"] = (
        aws_sdk_proton.types.service_instance.serialize_aws_json_1_0(
            value["service_instance"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetServiceInstanceOutput:
    out: GetServiceInstanceOutput = {}  # type: ignore[typeddict-item]
    if "serviceInstance" in data:
        import aws_sdk_proton.types.service_instance

        out["service_instance"] = (
            aws_sdk_proton.types.service_instance.deserialize_aws_json_1_0(
                data["serviceInstance"]
            )
        )
    else:
        raise DeserializationError("GetServiceInstanceOutput.service_instance required")
    return out
