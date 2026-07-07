"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#ValidateE911AddressResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.address
    import aws_sdk_chime_sdk_voice.types.candidate_address_list
    import aws_sdk_chime_sdk_voice.types.string
    import aws_sdk_chime_sdk_voice.types.validation_result


class ValidateE911AddressResponse(TypedDict, closed=True):
    validation_result: (
        "aws_sdk_chime_sdk_voice.types.validation_result.ValidationResult"
    )
    """<p>Number indicating the result of address validation.</p> <p>Each possible result is defined as follows:</p> <ul> <li> <p> <code>0</code> - Address validation succeeded.</p> </li> <li> <p> <code>1</code> - Address validation succeeded. The address was a close enough match and has been corrected as part of the address object.</p> </li> <li> <p> <code>2</code> - Address validation failed. You should re-submit the validation request with candidates from the <code>CandidateAddressList</code> result, if it's a close match.</p> </li> </ul>"""
    address_external_id: NotRequired["aws_sdk_chime_sdk_voice.types.string.String"]
    """<p>The ID that represents the address.</p>"""
    address: NotRequired["aws_sdk_chime_sdk_voice.types.address.Address"]
    """<p>The validated address.</p>"""
    candidate_address_list: NotRequired[
        "aws_sdk_chime_sdk_voice.types.candidate_address_list.CandidateAddressList"
    ]
    """<p>The list of address suggestions..</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidateE911AddressResponse) -> dict:
    out: dict = {}
    out["ValidationResult"] = value.get("validation_result", 0)
    if "address_external_id" in value:
        out["AddressExternalId"] = value["address_external_id"]
    if "address" in value:
        import aws_sdk_chime_sdk_voice.types.address

        out["Address"] = aws_sdk_chime_sdk_voice.types.address.serialize_json(
            value["address"]
        )
    if "candidate_address_list" in value:
        import aws_sdk_chime_sdk_voice.types.candidate_address_list

        out["CandidateAddressList"] = (
            aws_sdk_chime_sdk_voice.types.candidate_address_list.serialize_json(
                value["candidate_address_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> ValidateE911AddressResponse:
    out: ValidateE911AddressResponse = {}  # type: ignore[typeddict-item]
    if "ValidationResult" in data:
        out["validation_result"] = data["ValidationResult"]
    else:
        out["validation_result"] = 0
    if "AddressExternalId" in data:
        out["address_external_id"] = data["AddressExternalId"]
    if "Address" in data:
        import aws_sdk_chime_sdk_voice.types.address

        out["address"] = aws_sdk_chime_sdk_voice.types.address.deserialize_json(
            data["Address"]
        )
    if "CandidateAddressList" in data:
        import aws_sdk_chime_sdk_voice.types.candidate_address_list

        out["candidate_address_list"] = (
            aws_sdk_chime_sdk_voice.types.candidate_address_list.deserialize_json(
                data["CandidateAddressList"]
            )
        )
    return out
