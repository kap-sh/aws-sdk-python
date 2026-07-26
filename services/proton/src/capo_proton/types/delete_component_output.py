"""Generated from Smithy shape ``com.amazonaws.proton#DeleteComponentOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_proton.types.component


class DeleteComponentOutput(TypedDict, closed=True):
    component: NotRequired["capo_proton.types.component.Component"]
    """<p>The detailed data of the component being deleted.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteComponentOutput) -> dict:
    out: dict = {}
    if "component" in value:
        import capo_proton.types.component

        out["component"] = capo_proton.types.component.serialize_aws_json_1_0(
            value["component"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteComponentOutput:
    out: DeleteComponentOutput = {}  # type: ignore[typeddict-item]
    if "component" in data:
        import capo_proton.types.component

        out["component"] = capo_proton.types.component.deserialize_aws_json_1_0(
            data["component"]
        )
    return out
