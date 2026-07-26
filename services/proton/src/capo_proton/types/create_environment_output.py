"""Generated from Smithy shape ``com.amazonaws.proton#CreateEnvironmentOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_proton.errors import DeserializationError

if TYPE_CHECKING:
    import capo_proton.types.environment


class CreateEnvironmentOutput(TypedDict, closed=True):
    environment: "capo_proton.types.environment.Environment"
    """<p>The environment detail data that's returned by Proton.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateEnvironmentOutput) -> dict:
    out: dict = {}
    import capo_proton.types.environment

    out["environment"] = capo_proton.types.environment.serialize_aws_json_1_0(
        value["environment"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateEnvironmentOutput:
    out: CreateEnvironmentOutput = {}  # type: ignore[typeddict-item]
    if "environment" in data:
        import capo_proton.types.environment

        out["environment"] = capo_proton.types.environment.deserialize_aws_json_1_0(
            data["environment"]
        )
    else:
        raise DeserializationError("CreateEnvironmentOutput.environment required")
    return out
