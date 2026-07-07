"""Generated from Smithy shape ``com.amazonaws.deadline#CopyJobTemplateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.job_template_type


class CopyJobTemplateResponse(TypedDict, closed=True):
    template_type: "aws_sdk_deadline.types.job_template_type.JobTemplateType"
    """<p>The format of the job template, either <code>JSON</code> or <code>YAML</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CopyJobTemplateResponse) -> dict:
    out: dict = {}
    import aws_sdk_deadline.types.job_template_type

    out["templateType"] = aws_sdk_deadline.types.job_template_type.serialize_json(
        value["template_type"]
    )
    return out


def deserialize_json(data: dict) -> CopyJobTemplateResponse:
    out: CopyJobTemplateResponse = {}  # type: ignore[typeddict-item]
    if "templateType" in data:
        import aws_sdk_deadline.types.job_template_type

        out["template_type"] = (
            aws_sdk_deadline.types.job_template_type.deserialize_json(
                data["templateType"]
            )
        )
    else:
        raise DeserializationError("CopyJobTemplateResponse.template_type required")
    return out
