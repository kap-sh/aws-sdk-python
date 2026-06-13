"""Generated from Smithy shape ``com.amazonaws.securityagent#Step``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import datetime

    import aws_sdk_securityagent.types.step_name
    import aws_sdk_securityagent.types.step_status


class Step(TypedDict):
    name: NotRequired["aws_sdk_securityagent.types.step_name.StepName"]
    """<p>The name of the step. Valid values include PREFLIGHT, STATIC_ANALYSIS, PENTEST, and FINALIZING.</p>"""
    status: NotRequired["aws_sdk_securityagent.types.step_status.StepStatus"]
    """<p>The current status of the step.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The date and time the step was created, in UTC format.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The date and time the step was last updated, in UTC format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Step) -> dict:
    out: dict = {}
    if "name" in value:
        import aws_sdk_securityagent.types.step_name

        out["name"] = aws_sdk_securityagent.types.step_name.serialize_json(
            value["name"]
        )
    if "status" in value:
        import aws_sdk_securityagent.types.step_status

        out["status"] = aws_sdk_securityagent.types.step_status.serialize_json(
            value["status"]
        )
    if "created_at" in value:
        import aws_sdk_securityagent.types._prelude.timestamp

        out["createdAt"] = (
            aws_sdk_securityagent.types._prelude.timestamp.serialize_json(
                value["created_at"]
            )
        )
    if "updated_at" in value:
        import aws_sdk_securityagent.types._prelude.timestamp

        out["updatedAt"] = (
            aws_sdk_securityagent.types._prelude.timestamp.serialize_json(
                value["updated_at"]
            )
        )
    return out


def deserialize_json(data: dict) -> Step:
    out: Step = {}  # type: ignore[typeddict-item]
    if "name" in data:
        import aws_sdk_securityagent.types.step_name

        out["name"] = aws_sdk_securityagent.types.step_name.deserialize_json(
            data["name"]
        )
    if "status" in data:
        import aws_sdk_securityagent.types.step_status

        out["status"] = aws_sdk_securityagent.types.step_status.deserialize_json(
            data["status"]
        )
    if "createdAt" in data:
        import aws_sdk_securityagent.types._prelude.timestamp

        out["created_at"] = (
            aws_sdk_securityagent.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    if "updatedAt" in data:
        import aws_sdk_securityagent.types._prelude.timestamp

        out["updated_at"] = (
            aws_sdk_securityagent.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    return out
