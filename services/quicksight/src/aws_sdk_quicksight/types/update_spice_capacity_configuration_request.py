"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateSPICECapacityConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.purchase_mode


class UpdateSPICECapacityConfigurationRequest(TypedDict, closed=True):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the SPICE configuration that you want to update.</p>"""
    purchase_mode: "aws_sdk_quicksight.types.purchase_mode.PurchaseMode"
    """<p>Determines how SPICE capacity can be purchased. The following options are available. </p> <ul> <li> <p> <code>MANUAL</code>: SPICE capacity can only be purchased manually.</p> </li> <li> <p> <code>AUTO_PURCHASE</code>: Extra SPICE capacity is automatically purchased on your behalf as needed. SPICE capacity can also be purchased manually with this option.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSPICECapacityConfigurationRequest) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.purchase_mode

    out["PurchaseMode"] = aws_sdk_quicksight.types.purchase_mode.serialize_json(
        value["purchase_mode"]
    )
    return out


def deserialize_json(data: dict) -> UpdateSPICECapacityConfigurationRequest:
    out: UpdateSPICECapacityConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "PurchaseMode" in data:
        import aws_sdk_quicksight.types.purchase_mode

        out["purchase_mode"] = aws_sdk_quicksight.types.purchase_mode.deserialize_json(
            data["PurchaseMode"]
        )
    else:
        raise DeserializationError(
            "UpdateSPICECapacityConfigurationRequest.purchase_mode required"
        )
    return out
