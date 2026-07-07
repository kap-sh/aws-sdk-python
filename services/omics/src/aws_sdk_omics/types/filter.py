"""Generated from Smithy shape ``com.amazonaws.omics#Filter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_omics.types.arn_list
    import aws_sdk_omics.types.status_list
    import aws_sdk_omics.types.type_list


class Filter(TypedDict, closed=True):
    resource_arns: NotRequired["aws_sdk_omics.types.arn_list.ArnList"]
    """<p>Filter based on the Amazon Resource Number (ARN) of the resource. You can specify up to 10 values.</p>"""
    status: NotRequired["aws_sdk_omics.types.status_list.StatusList"]
    """<p>Filter based on the resource status. You can specify up to 10 values.</p>"""
    type: NotRequired["aws_sdk_omics.types.type_list.TypeList"]
    """<p>The type of resources to be filtered. You can specify one or more of the resource types.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Filter) -> dict:
    out: dict = {}
    if "resource_arns" in value:
        import aws_sdk_omics.types.arn_list

        out["resourceArns"] = aws_sdk_omics.types.arn_list.serialize_json(
            value["resource_arns"]
        )
    if "status" in value:
        import aws_sdk_omics.types.status_list

        out["status"] = aws_sdk_omics.types.status_list.serialize_json(value["status"])
    if "type" in value:
        import aws_sdk_omics.types.type_list

        out["type"] = aws_sdk_omics.types.type_list.serialize_json(value["type"])
    return out


def deserialize_json(data: dict) -> Filter:
    out: Filter = {}  # type: ignore[typeddict-item]
    if "resourceArns" in data:
        import aws_sdk_omics.types.arn_list

        out["resource_arns"] = aws_sdk_omics.types.arn_list.deserialize_json(
            data["resourceArns"]
        )
    if "status" in data:
        import aws_sdk_omics.types.status_list

        out["status"] = aws_sdk_omics.types.status_list.deserialize_json(data["status"])
    if "type" in data:
        import aws_sdk_omics.types.type_list

        out["type"] = aws_sdk_omics.types.type_list.deserialize_json(data["type"])
    return out
