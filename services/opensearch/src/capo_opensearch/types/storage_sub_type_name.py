"""Generated from Smithy shape ``com.amazonaws.opensearch#StorageSubTypeName``."""

from typing import TypeAlias

"""<p> Sub-type of the given EBS storage type. List of available sub-storage options. The <code>instance</code> storage type has no storage sub-type. The <code>ebs</code> storage type has the following valid sub-types: </p> <ul> <li> <p> <code>standard</code> </p> </li> <li> <p> <code>gp2</code> </p> </li> <li> <p> <code>gp3</code> </p> </li> <li> <p> <code>io1</code> </p> </li> </ul>"""
StorageSubTypeName: TypeAlias = str
