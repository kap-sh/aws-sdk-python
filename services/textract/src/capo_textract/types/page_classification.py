"""Generated from Smithy shape ``com.amazonaws.textract#PageClassification``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_textract.errors import DeserializationError

if TYPE_CHECKING:
    import capo_textract.types.prediction_list


class PageClassification(TypedDict, closed=True):
    page_type: "capo_textract.types.prediction_list.PredictionList"
    """<p>The class, or document type, assigned to a detected Page object. The class, or document type, assigned to a detected Page object.</p>"""
    page_number: "capo_textract.types.prediction_list.PredictionList"
    """<p> The page number the value was detected on, relative to Amazon Textract's starting position.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PageClassification) -> dict:
    out: dict = {}
    import capo_textract.types.prediction_list

    out["PageType"] = capo_textract.types.prediction_list.serialize_aws_json_1_1(
        value["page_type"]
    )
    import capo_textract.types.prediction_list

    out["PageNumber"] = capo_textract.types.prediction_list.serialize_aws_json_1_1(
        value["page_number"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> PageClassification:
    out: PageClassification = {}  # type: ignore[typeddict-item]
    if "PageType" in data:
        import capo_textract.types.prediction_list

        out["page_type"] = capo_textract.types.prediction_list.deserialize_aws_json_1_1(
            data["PageType"]
        )
    else:
        raise DeserializationError("PageClassification.page_type required")
    if "PageNumber" in data:
        import capo_textract.types.prediction_list

        out["page_number"] = (
            capo_textract.types.prediction_list.deserialize_aws_json_1_1(
                data["PageNumber"]
            )
        )
    else:
        raise DeserializationError("PageClassification.page_number required")
    return out
