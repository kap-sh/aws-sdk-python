"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteEgressOnlyInternetGatewayResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean


class DeleteEgressOnlyInternetGatewayResult(TypedDict, closed=True):
    return_code: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Returns <code>true</code> if the request succeeds; otherwise, it returns an error.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteEgressOnlyInternetGatewayResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "return_code" in value:
        pairs.append(
            (f"{prefix}.ReturnCode", "true" if value["return_code"] else "false")
        )


def deserialize_ec2_query(el: Element) -> DeleteEgressOnlyInternetGatewayResult:
    out: DeleteEgressOnlyInternetGatewayResult = {}  # type: ignore[typeddict-item]
    child_return_code = el.find("ReturnCode")
    if child_return_code is not None:
        out["return_code"] = (child_return_code.text or "").lower() == "true"
    return out
