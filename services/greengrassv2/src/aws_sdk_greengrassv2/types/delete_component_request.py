"""Generated from Smithy shape ``com.amazonaws.greengrassv2#DeleteComponentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_greengrassv2.types.component_version_arn


class DeleteComponentRequest(TypedDict, closed=True):
    arn: "aws_sdk_greengrassv2.types.component_version_arn.ComponentVersionARN"
    r"""<p>The <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">ARN</a> of the component version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteComponentRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteComponentRequest:
    out: DeleteComponentRequest = {}  # type: ignore[typeddict-item]
    return out
