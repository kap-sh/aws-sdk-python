"""Generated from Smithy shape ``com.amazonaws.proton#CreateComponentOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_proton.errors import DeserializationError

if TYPE_CHECKING:
    import capo_proton.types.component


class CreateComponentOutput(TypedDict, closed=True):
    component: "capo_proton.types.component.Component"
    """<p>The detailed data of the created component.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateComponentOutput) -> dict:
    out: dict = {}
    import capo_proton.types.component

    out["component"] = capo_proton.types.component.serialize_aws_json_1_0(
        value["component"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateComponentOutput:
    out: CreateComponentOutput = {}  # type: ignore[typeddict-item]
    if "component" in data:
        import capo_proton.types.component

        out["component"] = capo_proton.types.component.deserialize_aws_json_1_0(
            data["component"]
        )
    else:
        raise DeserializationError("CreateComponentOutput.component required")
    return out
