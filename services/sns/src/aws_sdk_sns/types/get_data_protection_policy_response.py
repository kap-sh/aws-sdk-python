"""Generated from Smithy shape ``com.amazonaws.sns#GetDataProtectionPolicyResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sns._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_sns.types.attribute_value


class GetDataProtectionPolicyResponse(TypedDict):
    data_protection_policy: NotRequired[
        "aws_sdk_sns.types.attribute_value.attributeValue"
    ]
    """<p>Retrieves the <code>DataProtectionPolicy</code> in JSON string format.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetDataProtectionPolicyResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "data_protection_policy" in value:
        pairs.append(
            (f"{prefix}.DataProtectionPolicy", str(value["data_protection_policy"]))
        )


def deserialize_query(el: Element) -> GetDataProtectionPolicyResponse:
    out: GetDataProtectionPolicyResponse = {}  # type: ignore[typeddict-item]
    child_data_protection_policy = el.find("DataProtectionPolicy")
    if child_data_protection_policy is not None:
        out["data_protection_policy"] = str(child_data_protection_policy.text or "")
    return out
