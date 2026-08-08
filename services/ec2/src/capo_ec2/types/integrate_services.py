"""Generated from Smithy shape ``com.amazonaws.ec2#IntegrateServices``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.athena_integrations_set


class IntegrateServices(TypedDict, closed=True):
    athena_integrations: NotRequired[
        "capo_ec2.types.athena_integrations_set.AthenaIntegrationsSet"
    ]
    """<p>Information about the integration with Amazon Athena.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IntegrateServices, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "athena_integrations" in value:
        import capo_ec2.types.athena_integrations_set

        capo_ec2.types.athena_integrations_set.serialize_ec2_query(
            value["athena_integrations"], pairs, f"{key_prefix}AthenaIntegration"
        )


def deserialize_ec2_query(el: Element) -> IntegrateServices:
    out: IntegrateServices = {}  # type: ignore[typeddict-item]
    if el.find("AthenaIntegration") is not None:
        import capo_ec2.types.athena_integrations_set

        out["athena_integrations"] = (
            capo_ec2.types.athena_integrations_set.deserialize_ec2_query(
                el, "AthenaIntegration"
            )
        )
    return out
