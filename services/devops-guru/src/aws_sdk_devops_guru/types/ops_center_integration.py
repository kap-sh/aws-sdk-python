"""Generated from Smithy shape ``com.amazonaws.devopsguru#OpsCenterIntegration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.opt_in_status


class OpsCenterIntegration(TypedDict, closed=True):
    opt_in_status: NotRequired["aws_sdk_devops_guru.types.opt_in_status.OptInStatus"]
    """<p> Specifies if DevOps Guru is enabled to create an Amazon Web Services Systems Manager OpsItem for each created insight. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OpsCenterIntegration) -> dict:
    out: dict = {}
    if "opt_in_status" in value:
        import aws_sdk_devops_guru.types.opt_in_status

        out["OptInStatus"] = aws_sdk_devops_guru.types.opt_in_status.serialize_json(
            value["opt_in_status"]
        )
    return out


def deserialize_json(data: dict) -> OpsCenterIntegration:
    out: OpsCenterIntegration = {}  # type: ignore[typeddict-item]
    if "OptInStatus" in data:
        import aws_sdk_devops_guru.types.opt_in_status

        out["opt_in_status"] = aws_sdk_devops_guru.types.opt_in_status.deserialize_json(
            data["OptInStatus"]
        )
    return out
