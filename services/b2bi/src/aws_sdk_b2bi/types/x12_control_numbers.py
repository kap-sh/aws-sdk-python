"""Generated from Smithy shape ``com.amazonaws.b2bi#X12ControlNumbers``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_b2bi.types.starting_functional_group_control_number
    import aws_sdk_b2bi.types.starting_interchange_control_number
    import aws_sdk_b2bi.types.starting_transaction_set_control_number


class X12ControlNumbers(TypedDict):
    starting_interchange_control_number: NotRequired[
        "aws_sdk_b2bi.types.starting_interchange_control_number.StartingInterchangeControlNumber"
    ]
    """<p>Specifies the starting interchange control number (ISA13) to use for X12 EDI generation. This number is incremented for each new interchange. For the ISA (interchange) envelope, Amazon Web Services B2B Data Interchange generates an interchange control number that is unique for the ISA05 and ISA06 (sender) &amp; ISA07 and ISA08 (receiver) combination. </p>"""
    starting_functional_group_control_number: NotRequired[
        "aws_sdk_b2bi.types.starting_functional_group_control_number.StartingFunctionalGroupControlNumber"
    ]
    """<p>Specifies the starting functional group control number (GS06) to use for X12 EDI generation. This number is incremented for each new functional group. For the GS (functional group) envelope, Amazon Web Services B2B Data Interchange generates a functional group control number that is unique to the sender ID, receiver ID, and functional identifier code combination. </p>"""
    starting_transaction_set_control_number: NotRequired[
        "aws_sdk_b2bi.types.starting_transaction_set_control_number.StartingTransactionSetControlNumber"
    ]
    """<p>Specifies the starting transaction set control number (ST02) to use for X12 EDI generation. This number is incremented for each new transaction set.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: X12ControlNumbers) -> dict:
    out: dict = {}
    if "starting_interchange_control_number" in value:
        out["startingInterchangeControlNumber"] = value[
            "starting_interchange_control_number"
        ]
    if "starting_functional_group_control_number" in value:
        out["startingFunctionalGroupControlNumber"] = value[
            "starting_functional_group_control_number"
        ]
    if "starting_transaction_set_control_number" in value:
        out["startingTransactionSetControlNumber"] = value[
            "starting_transaction_set_control_number"
        ]
    return out


def deserialize_aws_json_1_0(data: dict) -> X12ControlNumbers:
    out: X12ControlNumbers = {}  # type: ignore[typeddict-item]
    if "startingInterchangeControlNumber" in data:
        out["starting_interchange_control_number"] = data[
            "startingInterchangeControlNumber"
        ]
    if "startingFunctionalGroupControlNumber" in data:
        out["starting_functional_group_control_number"] = data[
            "startingFunctionalGroupControlNumber"
        ]
    if "startingTransactionSetControlNumber" in data:
        out["starting_transaction_set_control_number"] = data[
            "startingTransactionSetControlNumber"
        ]
    return out
