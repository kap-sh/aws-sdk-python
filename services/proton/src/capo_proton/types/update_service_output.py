"""Generated from Smithy shape ``com.amazonaws.proton#UpdateServiceOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_proton.errors import DeserializationError

if TYPE_CHECKING:
    import capo_proton.types.service


class UpdateServiceOutput(TypedDict, closed=True):
    service: "capo_proton.types.service.Service"
    """<p>The service detail data that's returned by Proton.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateServiceOutput) -> dict:
    out: dict = {}
    import capo_proton.types.service

    out["service"] = capo_proton.types.service.serialize_aws_json_1_0(value["service"])
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateServiceOutput:
    out: UpdateServiceOutput = {}  # type: ignore[typeddict-item]
    if "service" in data:
        import capo_proton.types.service

        out["service"] = capo_proton.types.service.deserialize_aws_json_1_0(
            data["service"]
        )
    else:
        raise DeserializationError("UpdateServiceOutput.service required")
    return out
