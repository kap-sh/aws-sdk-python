"""Generated from Smithy shape ``com.amazonaws.ec2#ElasticInferenceAcceleratorAssociation``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.date_time
    import aws_sdk_ec2.types.string


class ElasticInferenceAcceleratorAssociation(TypedDict):
    elastic_inference_accelerator_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p> The Amazon Resource Name (ARN) of the elastic inference accelerator. </p>"""
    elastic_inference_accelerator_association_id: NotRequired[
        "aws_sdk_ec2.types.string.String"
    ]
    """<p> The ID of the association. </p>"""
    elastic_inference_accelerator_association_state: NotRequired[
        "aws_sdk_ec2.types.string.String"
    ]
    """<p> The state of the elastic inference accelerator. </p>"""
    elastic_inference_accelerator_association_time: NotRequired[
        "aws_sdk_ec2.types.date_time.DateTime"
    ]
    """<p> The time at which the elastic inference accelerator is associated with an instance. </p>"""
