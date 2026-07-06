"""Generated from Smithy shape ``com.amazonaws.route53recoveryreadiness#CreateCellRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_route53_recovery_readiness.types.__list_of__string
    import aws_sdk_route53_recovery_readiness.types.__string
    import aws_sdk_route53_recovery_readiness.types.tags


class CreateCellRequest(TypedDict, closed=True):
    cell_name: NotRequired["aws_sdk_route53_recovery_readiness.types.__string.__string"]
    """<p>The name of the cell to create.</p>"""
    cells: NotRequired[
        "aws_sdk_route53_recovery_readiness.types.__list_of__string.__listOf__string"
    ]
    """<p>A list of cell Amazon Resource Names (ARNs) contained within this cell, for use in nested cells. For example, Availability Zones within specific Amazon Web Services Regions.</p>"""
    tags: NotRequired["aws_sdk_route53_recovery_readiness.types.tags.Tags"]


# --- restJson1 ser/de ---
def serialize_json(value: CreateCellRequest) -> dict:
    out: dict = {}
    if "cell_name" in value:
        out["cellName"] = value["cell_name"]
    if "cells" in value:
        import aws_sdk_route53_recovery_readiness.types.__list_of__string

        out["cells"] = (
            aws_sdk_route53_recovery_readiness.types.__list_of__string.serialize_json(
                value["cells"]
            )
        )
    if "tags" in value:
        import aws_sdk_route53_recovery_readiness.types.tags

        out["tags"] = aws_sdk_route53_recovery_readiness.types.tags.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateCellRequest:
    out: CreateCellRequest = {}  # type: ignore[typeddict-item]
    if "cellName" in data:
        out["cell_name"] = data["cellName"]
    if "cells" in data:
        import aws_sdk_route53_recovery_readiness.types.__list_of__string

        out["cells"] = (
            aws_sdk_route53_recovery_readiness.types.__list_of__string.deserialize_json(
                data["cells"]
            )
        )
    if "tags" in data:
        import aws_sdk_route53_recovery_readiness.types.tags

        out["tags"] = aws_sdk_route53_recovery_readiness.types.tags.deserialize_json(
            data["tags"]
        )
    return out
