"""Generated from Smithy shape ``com.amazonaws.route53recoveryreadiness#CreateCellResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53_recovery_readiness.types.__list_of__string
    import capo_route53_recovery_readiness.types.__string_max64_pattern_aazaz09_z
    import capo_route53_recovery_readiness.types.__string_max256
    import capo_route53_recovery_readiness.types.tags


class CreateCellResponse(TypedDict, closed=True):
    cell_arn: NotRequired[
        "capo_route53_recovery_readiness.types.__string_max256.__stringMax256"
    ]
    """<p>The Amazon Resource Name (ARN) for the cell.</p>"""
    cell_name: NotRequired[
        "capo_route53_recovery_readiness.types.__string_max64_pattern_aazaz09_z.__stringMax64PatternAAZAZ09Z"
    ]
    """<p>The name of the cell.</p>"""
    cells: NotRequired[
        "capo_route53_recovery_readiness.types.__list_of__string.__listOf__string"
    ]
    """<p>A list of cell ARNs.</p>"""
    parent_readiness_scopes: NotRequired[
        "capo_route53_recovery_readiness.types.__list_of__string.__listOf__string"
    ]
    """<p>The readiness scope for the cell, which can be a cell Amazon Resource Name (ARN) or a recovery group ARN. This is a list but currently can have only one element.</p>"""
    tags: NotRequired["capo_route53_recovery_readiness.types.tags.Tags"]
    """<p>Tags on the resources.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCellResponse) -> dict:
    out: dict = {}
    if "cell_arn" in value:
        out["cellArn"] = value["cell_arn"]
    if "cell_name" in value:
        out["cellName"] = value["cell_name"]
    if "cells" in value:
        import capo_route53_recovery_readiness.types.__list_of__string

        out["cells"] = (
            capo_route53_recovery_readiness.types.__list_of__string.serialize_json(
                value["cells"]
            )
        )
    if "parent_readiness_scopes" in value:
        import capo_route53_recovery_readiness.types.__list_of__string

        out["parentReadinessScopes"] = (
            capo_route53_recovery_readiness.types.__list_of__string.serialize_json(
                value["parent_readiness_scopes"]
            )
        )
    if "tags" in value:
        import capo_route53_recovery_readiness.types.tags

        out["tags"] = capo_route53_recovery_readiness.types.tags.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateCellResponse:
    out: CreateCellResponse = {}  # type: ignore[typeddict-item]
    if "cellArn" in data:
        out["cell_arn"] = data["cellArn"]
    if "cellName" in data:
        out["cell_name"] = data["cellName"]
    if "cells" in data:
        import capo_route53_recovery_readiness.types.__list_of__string

        out["cells"] = (
            capo_route53_recovery_readiness.types.__list_of__string.deserialize_json(
                data["cells"]
            )
        )
    if "parentReadinessScopes" in data:
        import capo_route53_recovery_readiness.types.__list_of__string

        out["parent_readiness_scopes"] = (
            capo_route53_recovery_readiness.types.__list_of__string.deserialize_json(
                data["parentReadinessScopes"]
            )
        )
    if "tags" in data:
        import capo_route53_recovery_readiness.types.tags

        out["tags"] = capo_route53_recovery_readiness.types.tags.deserialize_json(
            data["tags"]
        )
    return out
