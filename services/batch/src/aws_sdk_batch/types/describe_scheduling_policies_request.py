"""Generated from Smithy shape ``com.amazonaws.batch#DescribeSchedulingPoliciesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_batch.types.string_list


class DescribeSchedulingPoliciesRequest(TypedDict, closed=True):
    arns: NotRequired["aws_sdk_batch.types.string_list.StringList"]
    """<p>A list of up to 100 scheduling policy Amazon Resource Name (ARN) entries.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeSchedulingPoliciesRequest) -> dict:
    out: dict = {}
    if "arns" in value:
        import aws_sdk_batch.types.string_list

        out["arns"] = aws_sdk_batch.types.string_list.serialize_json(value["arns"])
    return out


def deserialize_json(data: dict) -> DescribeSchedulingPoliciesRequest:
    out: DescribeSchedulingPoliciesRequest = {}  # type: ignore[typeddict-item]
    if "arns" in data:
        import aws_sdk_batch.types.string_list

        out["arns"] = aws_sdk_batch.types.string_list.deserialize_json(data["arns"])
    return out
