"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyVerifiedAccessInstanceLoggingConfigurationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.verified_access_instance_logging_configuration


class ModifyVerifiedAccessInstanceLoggingConfigurationResult(TypedDict, closed=True):
    logging_configuration: NotRequired[
        "capo_ec2.types.verified_access_instance_logging_configuration.VerifiedAccessInstanceLoggingConfiguration"
    ]
    """<p>The logging configuration for the Verified Access instance.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyVerifiedAccessInstanceLoggingConfigurationResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "logging_configuration" in value:
        import capo_ec2.types.verified_access_instance_logging_configuration

        capo_ec2.types.verified_access_instance_logging_configuration.serialize_ec2_query(
            value["logging_configuration"], pairs, f"{key_prefix}LoggingConfiguration"
        )


def deserialize_ec2_query(
    el: Element,
) -> ModifyVerifiedAccessInstanceLoggingConfigurationResult:
    out: ModifyVerifiedAccessInstanceLoggingConfigurationResult = {}  # type: ignore[typeddict-item]
    child_logging_configuration = el.find("loggingConfiguration")
    if child_logging_configuration is not None:
        import capo_ec2.types.verified_access_instance_logging_configuration

        out["logging_configuration"] = (
            capo_ec2.types.verified_access_instance_logging_configuration.deserialize_ec2_query(
                child_logging_configuration
            )
        )
    return out
