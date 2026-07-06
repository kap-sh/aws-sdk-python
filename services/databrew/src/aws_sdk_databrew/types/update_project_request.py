"""Generated from Smithy shape ``com.amazonaws.databrew#UpdateProjectRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_databrew.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_databrew.types.arn
    import aws_sdk_databrew.types.project_name
    import aws_sdk_databrew.types.sample


class UpdateProjectRequest(TypedDict, closed=True):
    sample: NotRequired["aws_sdk_databrew.types.sample.Sample"]
    role_arn: "aws_sdk_databrew.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the IAM role to be assumed for this request.</p>"""
    name: "aws_sdk_databrew.types.project_name.ProjectName"
    """<p>The name of the project to be updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateProjectRequest) -> dict:
    out: dict = {}
    if "sample" in value:
        import aws_sdk_databrew.types.sample

        out["Sample"] = aws_sdk_databrew.types.sample.serialize_json(value["sample"])
    out["RoleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> UpdateProjectRequest:
    out: UpdateProjectRequest = {}  # type: ignore[typeddict-item]
    if "Sample" in data:
        import aws_sdk_databrew.types.sample

        out["sample"] = aws_sdk_databrew.types.sample.deserialize_json(data["Sample"])
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    else:
        raise DeserializationError("UpdateProjectRequest.role_arn required")
    return out
