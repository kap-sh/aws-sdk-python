"""Generated from Smithy shape ``com.amazonaws.ssm#UnlabelParameterVersionResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.parameter_label_list


class UnlabelParameterVersionResult(TypedDict, closed=True):
    removed_labels: NotRequired[
        "capo_ssm.types.parameter_label_list.ParameterLabelList"
    ]
    """<p>A list of all labels deleted from the parameter.</p>"""
    invalid_labels: NotRequired[
        "capo_ssm.types.parameter_label_list.ParameterLabelList"
    ]
    """<p>The labels that aren't attached to the given parameter version.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnlabelParameterVersionResult) -> dict:
    out: dict = {}
    if "removed_labels" in value:
        import capo_ssm.types.parameter_label_list

        out["RemovedLabels"] = (
            capo_ssm.types.parameter_label_list.serialize_aws_json_1_1(
                value["removed_labels"]
            )
        )
    if "invalid_labels" in value:
        import capo_ssm.types.parameter_label_list

        out["InvalidLabels"] = (
            capo_ssm.types.parameter_label_list.serialize_aws_json_1_1(
                value["invalid_labels"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UnlabelParameterVersionResult:
    out: UnlabelParameterVersionResult = {}  # type: ignore[typeddict-item]
    if data.get("RemovedLabels") is not None:
        import capo_ssm.types.parameter_label_list

        out["removed_labels"] = (
            capo_ssm.types.parameter_label_list.deserialize_aws_json_1_1(
                data["RemovedLabels"]
            )
        )
    if data.get("InvalidLabels") is not None:
        import capo_ssm.types.parameter_label_list

        out["invalid_labels"] = (
            capo_ssm.types.parameter_label_list.deserialize_aws_json_1_1(
                data["InvalidLabels"]
            )
        )
    return out
