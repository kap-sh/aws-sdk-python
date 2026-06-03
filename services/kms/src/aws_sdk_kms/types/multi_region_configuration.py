"""Generated from Smithy shape ``com.amazonaws.kms#MultiRegionConfiguration``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kms.types.multi_region_key
    import aws_sdk_kms.types.multi_region_key_list
    import aws_sdk_kms.types.multi_region_key_type


class MultiRegionConfiguration(TypedDict):
    multi_region_key_type: NotRequired[
        "aws_sdk_kms.types.multi_region_key_type.MultiRegionKeyType"
    ]
    """<p>Indicates whether the KMS key is a <code>PRIMARY</code> or <code>REPLICA</code> key.</p>"""
    primary_key: NotRequired["aws_sdk_kms.types.multi_region_key.MultiRegionKey"]
    """<p>Displays the key ARN and Region of the primary key. This field includes the current KMS key if it is the primary key.</p>"""
    replica_keys: NotRequired[
        "aws_sdk_kms.types.multi_region_key_list.MultiRegionKeyList"
    ]
    """<p>displays the key ARNs and Regions of all replica keys. This field includes the current KMS key if it is a replica key.</p>"""
