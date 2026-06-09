"""Generated from Smithy shape ``com.amazonaws.ec2#UnsuccessfulInstanceCreditSpecificationItemError``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.unsuccessful_instance_credit_specification_error_code


class UnsuccessfulInstanceCreditSpecificationItemError(TypedDict):
    code: NotRequired[
        "aws_sdk_ec2.types.unsuccessful_instance_credit_specification_error_code.UnsuccessfulInstanceCreditSpecificationErrorCode"
    ]
    """<p>The error code.</p>"""
    message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The applicable error message.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: UnsuccessfulInstanceCreditSpecificationItemError,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "code" in value:
        import aws_sdk_ec2.types.unsuccessful_instance_credit_specification_error_code

        aws_sdk_ec2.types.unsuccessful_instance_credit_specification_error_code.serialize_ec2_query(
            value["code"], pairs, f"{prefix}.Code"
        )
    if "message" in value:
        pairs.append((f"{prefix}.Message", str(value["message"])))


def deserialize_ec2_query(
    el: Element,
) -> UnsuccessfulInstanceCreditSpecificationItemError:
    out: UnsuccessfulInstanceCreditSpecificationItemError = {}  # type: ignore[typeddict-item]
    child_code = el.find("Code")
    if child_code is not None:
        import aws_sdk_ec2.types.unsuccessful_instance_credit_specification_error_code

        out["code"] = (
            aws_sdk_ec2.types.unsuccessful_instance_credit_specification_error_code.deserialize_ec2_query(
                child_code
            )
        )
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out
