"""Generated from Smithy shape ``com.amazonaws.proton#UpdateServiceInstanceOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_proton.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_proton.types.service_instance


class UpdateServiceInstanceOutput(TypedDict):
    service_instance: "aws_sdk_proton.types.service_instance.ServiceInstance"
    """<p>The service instance summary data that's returned by Proton.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateServiceInstanceOutput) -> dict:
    out: dict = {}
    import aws_sdk_proton.types.service_instance

    out["serviceInstance"] = (
        aws_sdk_proton.types.service_instance.serialize_aws_json_1_0(
            value["service_instance"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateServiceInstanceOutput:
    out: UpdateServiceInstanceOutput = {}  # type: ignore[typeddict-item]
    if "serviceInstance" in data:
        import aws_sdk_proton.types.service_instance

        out["service_instance"] = (
            aws_sdk_proton.types.service_instance.deserialize_aws_json_1_0(
                data["serviceInstance"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateServiceInstanceOutput.service_instance required"
        )
    return out
