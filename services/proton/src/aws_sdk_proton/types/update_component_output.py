"""Generated from Smithy shape ``com.amazonaws.proton#UpdateComponentOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_proton.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_proton.types.component


class UpdateComponentOutput(TypedDict, closed=True):
    component: "aws_sdk_proton.types.component.Component"
    """<p>The detailed data of the updated component.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateComponentOutput) -> dict:
    out: dict = {}
    import aws_sdk_proton.types.component

    out["component"] = aws_sdk_proton.types.component.serialize_aws_json_1_0(
        value["component"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateComponentOutput:
    out: UpdateComponentOutput = {}  # type: ignore[typeddict-item]
    if "component" in data:
        import aws_sdk_proton.types.component

        out["component"] = aws_sdk_proton.types.component.deserialize_aws_json_1_0(
            data["component"]
        )
    else:
        raise DeserializationError("UpdateComponentOutput.component required")
    return out
