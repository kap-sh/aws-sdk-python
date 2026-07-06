"""Generated from Smithy shape ``com.amazonaws.route53recoveryreadiness#ListCellsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_route53_recovery_readiness.types.__list_of_cell_output
    import aws_sdk_route53_recovery_readiness.types.__string


class ListCellsResponse(TypedDict, closed=True):
    cells: NotRequired[
        "aws_sdk_route53_recovery_readiness.types.__list_of_cell_output.__listOfCellOutput"
    ]
    """<p>A list of cells.</p>"""
    next_token: NotRequired[
        "aws_sdk_route53_recovery_readiness.types.__string.__string"
    ]
    """<p>The token that identifies which batch of results you want to see.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCellsResponse) -> dict:
    out: dict = {}
    if "cells" in value:
        import aws_sdk_route53_recovery_readiness.types.__list_of_cell_output

        out["cells"] = (
            aws_sdk_route53_recovery_readiness.types.__list_of_cell_output.serialize_json(
                value["cells"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListCellsResponse:
    out: ListCellsResponse = {}  # type: ignore[typeddict-item]
    if "cells" in data:
        import aws_sdk_route53_recovery_readiness.types.__list_of_cell_output

        out["cells"] = (
            aws_sdk_route53_recovery_readiness.types.__list_of_cell_output.deserialize_json(
                data["cells"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
