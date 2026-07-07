"""Generated from Smithy shape ``com.amazonaws.quicksight#DashboardSourceTemplate``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.arn
    import aws_sdk_quicksight.types.data_set_reference_list


class DashboardSourceTemplate(TypedDict, closed=True):
    data_set_references: (
        "aws_sdk_quicksight.types.data_set_reference_list.DataSetReferenceList"
    )
    """<p>Dataset references.</p>"""
    arn: "aws_sdk_quicksight.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DashboardSourceTemplate) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.data_set_reference_list

    out["DataSetReferences"] = (
        aws_sdk_quicksight.types.data_set_reference_list.serialize_json(
            value["data_set_references"]
        )
    )
    out["Arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> DashboardSourceTemplate:
    out: DashboardSourceTemplate = {}  # type: ignore[typeddict-item]
    if "DataSetReferences" in data:
        import aws_sdk_quicksight.types.data_set_reference_list

        out["data_set_references"] = (
            aws_sdk_quicksight.types.data_set_reference_list.deserialize_json(
                data["DataSetReferences"]
            )
        )
    else:
        raise DeserializationError(
            "DashboardSourceTemplate.data_set_references required"
        )
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("DashboardSourceTemplate.arn required")
    return out
