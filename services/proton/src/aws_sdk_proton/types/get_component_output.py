"""Generated from Smithy shape ``com.amazonaws.proton#GetComponentOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_proton.types.component


class GetComponentOutput(TypedDict, closed=True):
    component: NotRequired["aws_sdk_proton.types.component.Component"]
    """<p>The detailed data of the requested component.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetComponentOutput) -> dict:
    out: dict = {}
    if "component" in value:
        import aws_sdk_proton.types.component

        out["component"] = aws_sdk_proton.types.component.serialize_aws_json_1_0(
            value["component"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetComponentOutput:
    out: GetComponentOutput = {}  # type: ignore[typeddict-item]
    if "component" in data:
        import aws_sdk_proton.types.component

        out["component"] = aws_sdk_proton.types.component.deserialize_aws_json_1_0(
            data["component"]
        )
    return out
