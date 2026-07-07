"""Generated from Smithy shape ``com.amazonaws.appconfigdata#InvalidParameterDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appconfigdata.types.invalid_parameter_problem


class InvalidParameterDetail(TypedDict, closed=True):
    problem: NotRequired[
        "aws_sdk_appconfigdata.types.invalid_parameter_problem.InvalidParameterProblem"
    ]
    """<p>The reason the parameter is invalid.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvalidParameterDetail) -> dict:
    out: dict = {}
    if "problem" in value:
        out["Problem"] = value["problem"]
    return out


def deserialize_json(data: dict) -> InvalidParameterDetail:
    out: InvalidParameterDetail = {}  # type: ignore[typeddict-item]
    if "Problem" in data:
        out["problem"] = data["Problem"]
    return out
